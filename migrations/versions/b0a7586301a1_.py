"""empty message

Revision ID: b0a7586301a1
Revises: b05246b7ad30
Create Date: 2017-05-01 00:52:55.828743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b0a7586301a1'
down_revision = 'b05246b7ad30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batch',
    sa.Column('batch_id', sa.String(length=30), nullable=False),
    sa.Column('ssk_advisor_id', sa.String(length=30), nullable=True),
    sa.Column('verbal_advisor_id', sa.String(length=30), nullable=True),
    sa.Column('aptitude_advisor_id', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['aptitude_advisor_id'], ['advisor.employee_id'], ),
    sa.ForeignKeyConstraint(['ssk_advisor_id'], ['advisor.employee_id'], ),
    sa.ForeignKeyConstraint(['verbal_advisor_id'], ['advisor.employee_id'], ),
    sa.PrimaryKeyConstraint('batch_id')
    )
    op.add_column(u'advisor', sa.Column('employee_id', sa.String(length=30), nullable=False))
    op.create_index(op.f('ix_advisor_employee_id'), 'advisor', ['employee_id'], unique=False)
    op.drop_index('ix_advisor_id', table_name='advisor')
    op.drop_column(u'advisor', 'id')
    op.alter_column(u'feedback', 'semester',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column(u'feedback', 'student_id',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.add_column(u'student', sa.Column('batch_id', sa.String(length=30), nullable=True))
    op.create_foreign_key(None, 'student', 'batch', ['batch_id'], ['batch_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_column(u'student', 'batch_id')
    op.alter_column(u'feedback', 'student_id',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column(u'feedback', 'semester',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.add_column(u'advisor', sa.Column('id', mysql.VARCHAR(length=30), nullable=False))
    op.create_index('ix_advisor_id', 'advisor', ['id'], unique=False)
    op.drop_index(op.f('ix_advisor_employee_id'), table_name='advisor')
    op.drop_column(u'advisor', 'employee_id')
    op.drop_table('batch')
    # ### end Alembic commands ###
