import os
import importlib
from fastapi import FastAPI

app = FastAPI()

def register_routers(app: FastAPI):
  pastaControllers = os.path.join(os.path.dirname(__file__), "controllers")
  for filename in os.listdir(pastaControllers):
    if filename.endswith(".py") and filename != "__init__.py":
      controllerName = f"controllers.{filename[:-3]}"
      controller = importlib.import_module(controllerName)
      if hasattr(controller, "router"):
        app.include_router(controller.router)

register_routers(app)
