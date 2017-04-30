"""empty message

Revision ID: 9703fb64ecaa
Revises: 2dc0192b93ac
Create Date: 2017-05-01 01:44:11.051104

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9703fb64ecaa'
down_revision = '2dc0192b93ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('batch', sa.Column('batch_id', sa.String(length=30), nullable=False))
    op.drop_column('batch', 'batch')
    op.add_column('student', sa.Column('batch_id', sa.String(length=30), nullable=True))
    op.create_foreign_key(None, 'student', 'batch', ['batch_id'], ['batch_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_column('student', 'batch_id')
    op.add_column('batch', sa.Column('batch', mysql.VARCHAR(length=30), nullable=False))
    op.drop_column('batch', 'batch_id')
    # ### end Alembic commands ###