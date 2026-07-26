from typing import Optional

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

from supabase_client import supabase
from auth.dependencies import get_current_user

app = FastAPI(
    title="Auth API",
    description="Secure API with Supabase Auth — signup, login, logout, and protected routes.",
)


@app.on_event("startup")
async def startup_event():
    # Confirms the Supabase client initialized without throwing — the Stage 0 checkpoint.
    print("Server running and connected to Supabase")


# ---- Request schemas -------------------------------------------------------

class AuthPayload(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None


# ---- Public route -----------------------------------------------------------

@app.get("/public/info")
def public_info():
    return {"message": "Welcome stranger! This info is public."}


# ---- Auth routes --------------------------------------------------------------

@app.post("/auth/signup", status_code=201)
def signup(payload: AuthPayload):
    if not payload.email or not payload.password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    try:
        result = supabase.auth.sign_up(
            {"email": payload.email, "password": payload.password}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"user": result.user}


@app.post("/auth/login")
def login(payload: AuthPayload):
    if not payload.email or not payload.password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    try:
        result = supabase.auth.sign_in_with_password(
            {"email": payload.email, "password": payload.password}
        )
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid login credentials")

    if not result.session:
        raise HTTPException(status_code=401, detail="Invalid login credentials")

    return {
        "access_token": result.session.access_token,
        "refresh_token": result.session.refresh_token,
    }


@app.post("/auth/logout", status_code=204)
def logout(current_user=Depends(get_current_user)):
    try:
        supabase.auth.sign_out()
    except Exception:
        # Sign-out failing server-side shouldn't block the client from discarding its token
        pass
    return


# ---- Protected routes — both reuse the exact same guard --------------------

@app.get("/protected/profile")
def profile(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "created_at": current_user.created_at,
    }


@app.get("/protected/dashboard")
def dashboard(current_user=Depends(get_current_user)):
    # Stage 4 checkpoint: new protected route, zero new auth code — same guard reused.
    return {"message": f"Welcome to your dashboard, {current_user.email}"}


# ---- Bonus: a real 403 case (authorization, not just authentication) --------

ADMIN_EMAILS = {"admin@example.com"}  # swap for a real admin list / DB flag in production


@app.get("/protected/admin")
def admin_only(current_user=Depends(get_current_user)):
    if current_user.email not in ADMIN_EMAILS:
        raise HTTPException(status_code=403, detail="Admins only")
    return {"message": f"Welcome, admin {current_user.email}"}