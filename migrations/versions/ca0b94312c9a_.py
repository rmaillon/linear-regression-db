"""empty message

Revision ID: ca0b94312c9a
Revises: 
Create Date: 2020-08-04 09:52:14.778922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca0b94312c9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lin_reg_results',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(), nullable=True),
    sa.Column('YearsExperience', sa.Float(), nullable=True),
    sa.Column('Prediction', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lin_reg_results')
    # ### end Alembic commands ###
