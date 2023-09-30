from ninja import NinjaAPI, Router
from user.views import router as user_router

ninja_api = NinjaAPI(title='theinitium', docs_url='/docs')

# if api version is more complex, will create a package for several version
api_v1 = Router()
api_v1.add_router("user/", user_router)

ninja_api.add_router("api/v1", api_v1)
