import json
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Loan

@ensure_csrf_cookie
@require_http_methods(["GET", "POST"])
def loan_list(request):

    if request.method == "GET":
        loans = Loan.objects.all()

        data = []

        for loan in loans:
            data.append({
                "id": loan.id,
                "amount":str(loan.amount),
                "interest_rate": str(loan.interest_rate),
                "created_at": loan.created_at.isoformat()
            })
        return JsonResponse(data,safe=False)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except(json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse(
                {"error":"JSON invalido"},
                status = 400
            )   
    if not isinstance(data,dict):
        return JsonResponse(
            {"error": "Se esperaba un objeto JSON"},
            status=400
        )

    loan = Loan(
        amount=data.get("amount"),
        interest_rate=data.get("interest_rate")
    )

    try: 
        loan.full_clean()
    except (ValidationError,ValueError,TypeError) as error:
        if isinstance(error,ValidationError):
            return JsonResponse(
                {"errors": error.message_dict},
                status =400
            )

        return JsonResponse(
            {"error" : "Datos invalidos"},
            status=400
        )

    loan.save()

    return JsonResponse({
        "id": loan.id,
        "amount": str(loan.amount),
        "interest_rate":str(loan.interest_rate),
        "created_at": loan.created_at.isoformat()
    }, status=201)

            