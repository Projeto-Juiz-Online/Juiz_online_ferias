"""add time_of_submission to submissions

Revision ID: a4c9d2e1f7b3
Revises: 9f1c2c4e5b6a
Create Date: 2026-02-21 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4c9d2e1f7b3'
down_revision = '9f1c2c4e5b6a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('submissions', sa.Column('time_of_submission', sa.DateTime(), nullable=True))
    op.execute("UPDATE submissions SET time_of_submission = submitted_at WHERE time_of_submission IS NULL")
    with op.batch_alter_table('submissions', schema=None) as batch_op:
        batch_op.alter_column('time_of_submission', nullable=False)


def downgrade():
    with op.batch_alter_table('submissions', schema=None) as batch_op:
        batch_op.drop_column('time_of_submission')
