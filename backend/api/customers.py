from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.models.customer import Customer
from backend.schemas.customer import CustomerCreate, CustomerResponse


router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)





@router.post("/", response_model=CustomerResponse)
def create_customer(
    customer_data: CustomerCreate,
    db: Session = Depends(get_db),
):
    customer = Customer(
        full_name=customer_data.full_name,
        email=customer_data.email,
        phone=customer_data.phone,
    )

    db.add(customer)

    try:
        db.commit()
        db.refresh(customer)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="A customer with this email already exists.",
        )

    return customer


@router.get("/", response_model=list[CustomerResponse])
def get_customers(
    db: Session = Depends(get_db),
):
    customers = db.query(Customer).all()

    return customers

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db),
):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found.",
        )

    return customer