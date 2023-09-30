from ninja import Router

router = Router(tags=["user"])


@router.get("/hello")
def hello(_):
    return {"message": "Hello World!"}
