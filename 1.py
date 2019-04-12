# coding:utf-8
import time
class firs(object):
    @staticmethod
    def aaa(sec=5):
        try:
            time.sleep(sec)
        except Exception:
            raise
        #return sec


    def bbb(self,sec):
        a = self.aaa(sec=sec)
        print(a)


if __name__ == "__main__":

    q = firs()
    q.bbb(3)