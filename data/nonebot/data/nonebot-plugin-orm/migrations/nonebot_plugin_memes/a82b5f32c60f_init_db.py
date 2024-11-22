"""init_db

迁移 ID: a82b5f32c60f
父迁移:
创建时间: 2024-08-12 22:16:13.840860

"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "a82b5f32c60f"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = ("nonebot_plugin_memes",)
depends_on: str | Sequence[str] | None = "fff55366306e"


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_memes_memegenerationrecord",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("session_persist_id", sa.Integer(), nullable=False),
        sa.Column("time", sa.DateTime(), nullable=False),
        sa.Column("meme_key", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_nonebot_plugin_memes_memegenerationrecord")
        ),
    )
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_memes_memegenerationrecord")
    # ### end Alembic commands ###