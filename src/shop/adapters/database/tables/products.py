from sqlalchemy import func

from shop.adapters.database.meta import metadata
import sqlalchemy as sa

products_table = sa.Table(
    'products',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    sa.Column('title', sa.String, nullable=False),
    sa.Column('price', sa.DECIMAL, nullable=False),
    sa.Column(
        'created_at',
        sa.DateTime,
        server_default=func.now(),
        nullable=False,
    ),
    sa.Column(
        'updated_at',
        sa.DateTime,
        server_default=func.now(),
        nullable=False,
    ),
)
