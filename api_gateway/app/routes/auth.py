# api_gateway/app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from ..utils.auth import verify_password, create_jwt_token
from ..schemas import UserLogin, UserRegister

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register")
async def register(user: UserRegister):
    # Add user to database (pseudo-code)
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    return {"message": "User registered"}

@router.post("/login")
async def login(user: UserLogin):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_jwt_token({"sub": db_user.email})
    return {"token": token}