"""subscriber table update

Revision ID: fbc5fb88e4bc
Revises: 77053418650a
Create Date: 2022-07-13 21:20:22.872034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbc5fb88e4bc'
down_revision = '77053418650a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscriber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('confirm', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('unsubscribe', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscriber_email'), 'subscriber', ['email'], unique=True)
    op.create_index(op.f('ix_subscriber_first_name'), 'subscriber', ['first_name'], unique=False)
    op.create_index(op.f('ix_subscriber_last_name'), 'subscriber', ['last_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscriber_last_name'), table_name='subscriber')
    op.drop_index(op.f('ix_subscriber_first_name'), table_name='subscriber')
    op.drop_index(op.f('ix_subscriber_email'), table_name='subscriber')
    op.drop_table('subscriber')
    # ### end Alembic commands ###
