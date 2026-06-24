from pydantic import BaseModel , EmailStr
class UserCreate(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class TicketCreate(BaseModel):
    title : str
    description : str

class TicketUpdate(BaseModel):
    status : str



class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    company: str


class CustomerResponse(CustomerCreate):
    id: int

    class Config:
        from_attributes = True



class AgentCreate(BaseModel):
    name: str
    email: str
    department: str


class AgentResponse(AgentCreate):
    id: int

    class Config:
        from_attributes = True



class CommentCreate(BaseModel):
    ticket_id: int
    message: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str