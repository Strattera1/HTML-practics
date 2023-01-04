"""Initial migration.

Revision ID: b0e4a27cb04e
Revises: 
Create Date: 2023-01-03 12:21:15.833596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0e4a27cb04e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Products',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=50), nullable=False),
    sa.Column('Price', sa.Float(), nullable=False),
    sa.Column('Color', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Products')
    # ### end Alembic commands ###