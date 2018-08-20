from twisted.internet import protocol
from twisted.internet import reactor
import re
from sys import argv

if len(argv) != 2:
    print("Usage: spawner.py <image>")

pat = re.compile("HOSTADD  (.*)")


class Spawner(protocol.ProcessProtocol):
    def __init__(self):
        self.listening = True
        self.data = ""

    def connectionMade(self):
        self.transport.closeStdin()

    def outReceived(self, data):
        print(data.decode("utf-8"), end="")
        self.data = self.data + data.decode("utf-8")
        if self.listening and pat.match(self.data):
            print("\nADDING HOST ", list(pat.match(self.data).groups())[0])
            with open('/etc/hosts','w+') as f:
                f.write("\n")
                f.write(list(pat.match(self.data).groups())[0])
                f.write("\n")
            self.listening = False

    def errReceived(self, data):
        print("errReceived! with %d bytes!" % len(data))

    def inConnectionLost(self):
        print("inConnectionLost! stdin is closed! (we probably did it)")

    def outConnectionLost(self):
        print("outConnectionLost! The child closed their stdout!")

    def errConnectionLost(self):
        print("errConnectionLost! The child closed their stderr.")

    def processExited(self, reason):
        print("processExited, status %d" % (reason.value.exitCode,))

    def processEnded(self, reason):
        print("processEnded, status %d" % (reason.value.exitCode,))
        print("quitting")
        reactor.stop()


spawner = Spawner()
reactor.spawnProcess(spawner, "docker", ["docker", "run", "-t", argv[1]], {})
reactor.run()
