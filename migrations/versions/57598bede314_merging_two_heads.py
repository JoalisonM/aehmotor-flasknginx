"""merging two heads

Revision ID: 57598bede314
Revises: 8a76e59fd3bc, cab188b640a1
Create Date: 2023-11-09 11:21:15.823758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57598bede314'
down_revision = ('8a76e59fd3bc', 'cab188b640a1')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
