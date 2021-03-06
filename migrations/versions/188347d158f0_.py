"""empty message

Revision ID: 188347d158f0
Revises: 0f4a6c4d36c4
Create Date: 2019-02-23 20:39:03.879936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '188347d158f0'
down_revision = '0f4a6c4d36c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.create_foreign_key(None, 'todo', 'user', ['creator_id'], ['id'])
    op.drop_column('todo', 'creator')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('creator', sa.VARCHAR(length=64), nullable=True))
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.create_foreign_key(None, 'todo', 'user', ['creator'], ['id'])
    # ### end Alembic commands ###
