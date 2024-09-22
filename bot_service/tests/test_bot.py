import pytest
from aiogram import types
from infrastructure.telegram.bot_handler import handle_expense
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_handle_expense(mocker):

    mock_message = AsyncMock(spec=types.Message)
    mock_message.from_user.id = 12345
    mock_message.text = "Comida 50"
    mock_reply = mocker.patch.object(mock_message, 'reply', return_value=None)

    await handle_expense(mock_message)

    mock_reply.assert_called_with("Food expense added ✅")
