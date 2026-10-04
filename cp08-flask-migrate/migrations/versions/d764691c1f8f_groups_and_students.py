"""groups and students

Revision ID: d764691c1f8f
Revises: 
Create Date: 2026-10-04 17:20:38.993638

"""
from alembic import op
import sqlalchemy as sa


revision = 'd764691c1f8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=20), nullable=False),
    sa.Column('speciality', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=60), nullable=False),
    sa.Column('first_name', sa.String(length=60), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('hair', sa.String(length=30), nullable=True),
    sa.Column('eyes', sa.String(length=30), nullable=True),
    sa.Column('hobby', sa.String(length=80), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('student')
    op.drop_table('group')
