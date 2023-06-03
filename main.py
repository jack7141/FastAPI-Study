import os
import importlib
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse

# 기본 FastAPI 인스턴스
app = FastAPI(docs_url='/api/all/docs')
versioned_app = {}

# api/versioned 디렉토리를 탐색
folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'api', 'versioned')

for path, dirs, files in os.walk(folder):
    depth = path[len(folder) + len(os.path.sep):].count(os.path.sep)
    if path != folder and depth == 1 and '__init__.py' in files:
        _, version, api_name = path.split(os.path.sep)[-3:]

        _include = f"api.versioned.{version}.{api_name}"

        module = importlib.import_module(_include)

        # 버전별 FastAPI 인스턴스를 만들고 딕셔너리에 저장
        if version not in versioned_app:
            versioned_app[version] = FastAPI()

        versioned_app[version].include_router(module.router, prefix=f"/api/{version}/{api_name}")

        # 기본 FastAPI 인스턴스에도 라우터를 등록
        app.include_router(module.router, prefix=f"/api/{version}/{api_name}")
        app.docs_url = None  # 기본 FastAPI 인스턴스에서는 /docs를 사용하지 않음


@app.get("/api/{version}/docs", response_class=HTMLResponse)
async def swagger_ui_html(version: str):
    if version in versioned_app:
        openapi_url = f"/api/{version}/openapi.json"
        return get_swagger_ui_html(openapi_url=openapi_url, title=f"API {version}")
    else:
        return {"message": "Version not found"}


# 각 버전별 OpenAPI 스키마 생성
@app.get("/api/{version}/openapi.json")
async def get_open_api_endpoint(version: str):
    if version in versioned_app:
        return get_openapi(title=f"API Test {version}", version=version, routes=versioned_app[version].routes)
    else:
        return {"message": "Version not found"}
