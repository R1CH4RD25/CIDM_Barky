from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from dataclasses import dataclass
from typing import List

Base = declarative_base()

class DomainBookmark:
    """
    Pure domain bookmark:
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    notes TEXT,
    date_added TEXT NOT NULL    
    """
    def __init__(self, id, title, url, notes, date_added) -> None:
        self.id = id
        self.title = title
        self.url = url
        self.notes = notes
        self.date_added = date_added


class BookmarkModel(Base):
    """
    Declarative SQLA model
    """
    __tablename__ = 'bookmarks'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    url = Column(String(255))
    notes = Column(String(255))
    date_added = Column(Date)


@dataclass(unsafe_hash=True)
class Bookmark:

    id: int
    title: str
    url: str
    notes: str
    created_at: datetime
    updated_at: datetime
    
    def __init__(
        self,
        id: int,
        title: str,
        url: str,
        notes: str,
        created_at: datetime,
        updated_at: datetime
    ) -> None:
        self.id = id
        self.title = title
        self.url = url
        self.notes = notes
        self.created_at = created_at
        self.updated_at = updated_at
        self.events = []  # type: List[events.Event]

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }