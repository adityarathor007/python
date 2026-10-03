class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']]=None
Comment.model_rebuild()

comment=Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(id="1",content="reply 1")
        Comment(id="2",content="reply 1",replies=[
            Comment(id=4,content="nested reply")
        ]),
    ]
)