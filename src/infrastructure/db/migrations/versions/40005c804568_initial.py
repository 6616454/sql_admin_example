"""Initial

Revision ID: 40005c804568
Revises: 
Create Date: 2023-02-25 18:19:06.852205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40005c804568'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
