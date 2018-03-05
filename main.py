
from microWifi import MicroWifi
from machine   import Timer

# ============================================================================
# ===( Functions )============================================================
# ============================================================================

def _timerProcess(timer) :
	print('-----------------------------')
	print('AP  opened    : %s' % wifi.IsAccessPointOpened())
	print('STA connected : %s' % wifi.IsConnectedToAP())
	print('-----------------------------')

# ============================================================================
# ===( Main )=================================================================
# ============================================================================

print()
print("=======================================================================")
print()

print() # ----------------------------------------------

wifi = MicroWifi()

Timer.Alarm(_timerProcess, 3, periodic=True)

if not wifi.OpenAccessPointFromConf() :
	wifi.OpenAccessPoint('.-= AP TEST =-.', None, '192.168.0.254')

if not wifi.ConnectToAPFromConf() :
	wifi.ConnectToAP('JCzic', 'azerty123')

print()
print("=======================================================================")
print()

# ============================================================================
# ============================================================================
# ============================================================================


