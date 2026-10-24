from fastapi import APIRouter, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer

from create_user import UserRepository
from jwt_repository import CredentialsRepository
from schema import AccessTokenSchema

router = APIRouter(tags=["authorized"], prefix="/authorized")


get_token = OAuth2AuthorizationCodeBearer(tokenUrl="/authorized/login")


@router.post("/login")
async def login(
    repository_user: UserRepository = Depends(),
    credentials: OAuth2AuthorizationCodeBearer = Depends(),
    repository: CredentialsRepository = Depends(),
) -> AccessTokenSchema:
    user = repository_user.get_user(credentials.username, credentials.password)
    token = repository.make_token(user["nickname"])
    return AccessTokenSchema(access_token=token, token_type="Bearer")


@router.get("/data")
async def get_data(
    token: str = Depends(get_token),
    repository: CredentialsRepository = Depends(),
    repository_user: UserRepository = Depends(),
) -> str:
    username = repository.decode_token(token)
    if repository.is_valid_token(token):
        return repository_user.get_data_by_username(username)
    else:
        raise HTTP
