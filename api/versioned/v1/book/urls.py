from fastapi import APIRouter

router = APIRouter()

@router.get("/items", deprecated=True)
async def get_items():
    """
    사용자 정보를 읽는 API 엔드포인트입니다.
    """
    return ["Portal gun", "Plumbus"]


@router.get("/users", deprecated=True)
async def read_users():
    """
    사용자를 생성하는 API 엔드포인트입니다.
    """
    return ["Rick", "Morty"]


"""
오늘 커밋하거 없어서 그냥 git 명령어 외우기,,
git stash
git stash list
git stash pop
git stash drop
git stash apply targetname
git restore filepath
git restore --staged filepath
git branch -d name
git branch -D name

"""

