"""add example input/output columns to problems

Revision ID: be66b4a1eeb4
Revises: cc8b49e7c2a0
Create Date: 2026-02-14 09:54:09.786125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be66b4a1eeb4'
down_revision = 'cc8b49e7c2a0'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('problems', schema=None) as batch_op:
        batch_op.add_column(sa.Column('example_input', sa.Text(), nullable=False, server_default='Entrada de exemplo não cadastrada'))
        batch_op.add_column(sa.Column('example_output', sa.Text(), nullable=False, server_default='Saída de exemplo não cadastrada'))

    with op.batch_alter_table('problems', schema=None) as batch_op:
        batch_op.alter_column('example_input', server_default=None)
        batch_op.alter_column('example_output', server_default=None)


def downgrade():
    with op.batch_alter_table('problems', schema=None) as batch_op:
        batch_op.drop_column('example_output')
        batch_op.drop_column('example_input')
