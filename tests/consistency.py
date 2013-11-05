#!/usb/bin/py

import unittest

class ConsistencyTest(unittest.TestCase):

    def test(self):
        """Processors should return the same unordered results.
        """
        import processor.combinatory
        import processor.recursive
        import processor.tools
        args = {
            'source': 'cast',
            'target': 'cash',
            'maxlength': 4,
            'words': [w.strip() for w in processor.tools.read('words')],
            #'words': ['cast', 'hast', 'hart', 'hurt', 'hakk', 'hark', 'sark', 'surk', 'surt']
        }
        a = [e for e in processor.combinatory.find(**args)]
        b = [e for e in processor.recursive.find(**args)]
        a.sort()
        b.sort()
        self.assertEqual(a, b, "Processors did not return the same result")

if __name__ == '__main__':
    unittest.main()
