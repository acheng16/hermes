"""empty message

Revision ID: e5cbfa577206
Revises: None
Create Date: 2017-04-26 02:21:45.412418

"""

# revision identifiers, used by Alembic.
revision = 'e5cbfa577206'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=80), nullable=False),
    sa.Column('body', sa.String(length=1000), nullable=False),
    sa.Column('from_email', sa.String(length=80), nullable=False),
    sa.Column('recipient', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emails')
    ### end Alembic commands ###
