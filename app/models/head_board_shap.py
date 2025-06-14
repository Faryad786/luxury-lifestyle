from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.models.base import Base

class headBoardShape(Base):
    __tablename__ = "head_board_shaps"

    id = Column(Integer, primary_key=True, index=True)
    dimension = Column(String(20), nullable=False)  # Example: "3ft", "4ft"
    image = Column(String(500), nullable=False)
    size_id = Column(Integer, ForeignKey("sizes.id"), nullable=False)
    subcategory_id = Column(Integer, ForeignKey("subcategories.id"), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    size = relationship("Size", backref="head_board_shaps")
    subcategory = relationship("Subcategory", backref="head_board_shaps")

    def __repr__(self):
        return f"headBoardShape(id={self.id}, dimension={self.dimension}, image={self.image}, size_id={self.size_id}, subcategory_id={self.subcategory_id})"