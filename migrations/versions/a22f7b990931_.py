"""empty message

Revision ID: a22f7b990931
Revises: 9703fb64ecaa
Create Date: 2017-05-01 01:47:00.415732

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a22f7b990931'
down_revision = '9703fb64ecaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batch',
    sa.Column('batch_id', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('batch_id')
    )
    op.create_table('feedback',
    sa.Column('feedback_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=30), nullable=False),
    sa.Column('semester', sa.Integer(), nullable=False),
    sa.Column('quantitive_ability_score', sa.Integer(), nullable=True),
    sa.Column('quantitive_ability_feedback', sa.String(length=100), nullable=True),
    sa.Column('quantitive_ability_feedback_given_on', sa.DateTime(), nullable=True),
    sa.Column('quantitive_ability_feedback_given_by', sa.String(length=30), nullable=True),
    sa.Column('verbal_ability_score', sa.Integer(), nullable=True),
    sa.Column('verbal_ability_feedback', sa.String(length=100), nullable=True),
    sa.Column('verbal_ability_feedback_given_on', sa.DateTime(), nullable=True),
    sa.Column('verbal_ability_feedback_given_by', sa.String(length=30), nullable=True),
    sa.Column('soft_skills_score', sa.Integer(), nullable=True),
    sa.Column('soft_skills_feedback', sa.String(length=100), nullable=True),
    sa.Column('soft_skills_feeback_given_on', sa.DateTime(), nullable=True),
    sa.Column('soft_skills_feeback_given_by', sa.String(length=30), nullable=True),
    sa.Column('mock_gd_1_topic', sa.String(length=30), nullable=True),
    sa.Column('mock_gd_1_rating', sa.Integer(), nullable=True),
    sa.Column('mock_gd_1_feedback', sa.String(length=100), nullable=True),
    sa.Column('mock_gd_1_feedback_given_on', sa.DateTime(), nullable=True),
    sa.Column('mock_gd_1_feedback_given_by', sa.String(length=30), nullable=True),
    sa.Column('mock_gd_2_topic', sa.String(length=30), nullable=True),
    sa.Column('mock_gd_2_rating', sa.DateTime(), nullable=True),
    sa.Column('mock_gd_2_feedback', sa.String(length=100), nullable=True),
    sa.Column('mock_gd_2_feedback_given_on', sa.DateTime(), nullable=True),
    sa.Column('mock_gd_2_feedback_given_by', sa.String(length=30), nullable=True),
    sa.Column('mock_interview_1_topic', sa.String(length=30), nullable=True),
    sa.Column('mock_interview_1_rating', sa.Integer(), nullable=True),
    sa.Column('mock_interview_1_feedback', sa.String(length=100), nullable=True),
    sa.Column('mock_interview_1_feedback_given_on', sa.DateTime(), nullable=True),
    sa.Column('mock_interview_1_feedback_given_by', sa.String(length=30), nullable=True),
    sa.Column('mock_interview_2_topic', sa.String(length=30), nullable=True),
    sa.Column('mock_interview_2_rating', sa.Integer(), nullable=True),
    sa.Column('mock_interview_2_feedback', sa.String(length=100), nullable=True),
    sa.Column('mock_interview_2_feedback_given_on', sa.DateTime(), nullable=True),
    sa.Column('mock_interview_2_feedback_given_by', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.roll_number'], ),
    sa.PrimaryKeyConstraint('feedback_id')
    )
    op.add_column(u'advisor', sa.Column('employee_id', sa.String(length=30), nullable=False))
    op.create_index(op.f('ix_advisor_employee_id'), 'advisor', ['employee_id'], unique=False)
    op.drop_index('ix_advisor_id', table_name='advisor')
    op.drop_column(u'advisor', 'id')
    op.create_foreign_key(None, 'student', 'batch', ['batch_id'], ['batch_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.add_column(u'advisor', sa.Column('id', mysql.VARCHAR(length=30), nullable=False))
    op.create_index('ix_advisor_id', 'advisor', ['id'], unique=False)
    op.drop_index(op.f('ix_advisor_employee_id'), table_name='advisor')
    op.drop_column(u'advisor', 'employee_id')
    op.drop_table('feedback')
    op.drop_table('batch')
    # ### end Alembic commands ###
