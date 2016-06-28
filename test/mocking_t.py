import unittest.mock as mock

import imaplib
mock_IMAP4 = mock.create_autospec(imaplib.IMAP4_SSL)
# mock_IMAP4 = mock.MagicMock()
# imap_obj = mock_IMAP4('imap.seznam.cz',993)
imap_obj = mock_IMAP4('imap.seznam.cz')

# m_x = mock.Mock()
# m_x.return_value = 'xxx'
# print(m_x())

imap_obj.login.return_value = ['OK','some message']
resp, data = imap_obj.login('dfsdfsd','111')
# print(resp,data)
imap_obj.login.assert_called_with('dfsdfsd','111')