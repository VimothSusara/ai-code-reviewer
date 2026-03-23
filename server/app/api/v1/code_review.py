from fastapi import APIRouter

from app.schemas.code_review import CodeReviewRequest, CodeReviewResponse
from app.services.code_review_service import CodeReviewService

router = APIRouter()
code_reviewer_service = CodeReviewService()

@router.post("/", response_model=CodeReviewResponse)
async def code_review(request: CodeReviewRequest):

    result = await code_reviewer_service.generate_response(
        code=request.code,
        language=request.language
    )

    return CodeReviewResponse(review=result)