"""add belongs_only_to_contest to problems

Revision ID: d9ab3f9c1a21
Revises: be66b4a1eeb4
Create Date: 2026-02-17 18:05:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ab3f9c1a21'
down_revision = 'be66b4a1eeb4'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('problems', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('belongs_only_to_contest', sa.Boolean(), nullable=False, server_default=sa.false())
        )

    with op.batch_alter_table('problems', schema=None) as batch_op:
        batch_op.alter_column('belongs_only_to_contest', server_default=None)


def downgrade():
    with op.batch_alter_table('problems', schema=None) as batch_op:
        batch_op.drop_column('belongs_only_to_contest')
