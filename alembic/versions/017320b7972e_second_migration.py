"""Second migration

Revision ID: 017320b7972e
Revises: 83271fc34439
Create Date: 2024-12-03 00:59:51.797234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '017320b7972e'
down_revision = '83271fc34439'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meetingroom', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meetingroom', 'description')
    # ### end Alembic commands ###
