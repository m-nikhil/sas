"""empty message

Revision ID: b05246b7ad30
Revises: 65ad8290730f
Create Date: 2017-04-30 23:41:41.700980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b05246b7ad30'
down_revision = '65ad8290730f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('feedback_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=30), nullable=True),
    sa.Column('semester', sa.Integer(), nullable=True),
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    # ### end Alembic commands ###
