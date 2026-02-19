"""add points to contest registrations

Revision ID: 9f1c2c4e5b6a
Revises: 639cca735080
Create Date: 2026-02-19 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f1c2c4e5b6a'
down_revision = '639cca735080'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('contest_registrations', sa.Column('points', sa.Integer(), nullable=False, server_default='0'))
    op.alter_column('contest_registrations', 'points', server_default=None)


def downgrade():
    op.drop_column('contest_registrations', 'points')
