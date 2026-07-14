import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import app as app_module


class HasFechaModificacionTests(unittest.TestCase):
    def setUp(self):
        app_module.app.config.pop('HAS_FECHA_MOD', None)

    def test_uses_catalog_query_without_schema_constraint(self):
        fake_cursor = MagicMock()
        fake_cursor.fetchone.return_value = (True,)
        fake_conn = MagicMock()
        fake_conn.cursor.return_value = fake_cursor

        with patch.object(app_module, 'conectar_db', return_value=fake_conn):
            self.assertTrue(app_module.has_fecha_modificacion())

        executed_sql = fake_cursor.execute.call_args[0][0]
        self.assertIn('information_schema.columns', executed_sql)
        self.assertNotIn('table_schema', executed_sql.lower())


if __name__ == '__main__':
    unittest.main()
