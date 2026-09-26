import unittest
from core.permissions import PermissionManager
from core.registry import Tool, ToolRegistry

class CoreTests(unittest.TestCase):
    def test_permissions(self):
        p=PermissionManager()
        self.assertTrue(p.check("low").allowed)
        self.assertFalse(p.check("high").allowed)
        self.assertTrue(p.check("high",True).allowed)

    def test_registry(self):
        r=ToolRegistry(); r.register(Tool("x","test",lambda:"ok"))
        self.assertEqual(r.get("x").handler(),"ok")

if __name__=="__main__": unittest.main()
