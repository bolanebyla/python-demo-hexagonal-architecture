"""create table `products`

Revision ID: f1b53864ec42
Revises: 
Create Date: 2024-03-28 03:47:29.692354+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import func

# revision identifiers, used by Alembic.
revision = 'f1b53864ec42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
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


def downgrade():
    op.drop_table('products')
