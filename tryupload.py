# from app.utils.dataUtilsCode import uniqueClassSetAndDict,uniqueDictonairies,arrangeNnumberOfDictionary,returnList,writeListAsAJsonFile,makeinfodatabasewritable
# from app.darkflowMerge.openCVTFNet import extractFrameInfosFromVideo,extractIndicesFromTuple,frameToVid
from datetime import datetime


listOfResultsWithTuple = [([{'label': 'chair', 'confidence': 0.141772, 'topleft': {'x': 4, 'y': 21}, 'bottomright': {'x': 197, 'y': 339}}, {'label': 'diningtable', 'confidence': 0.29719263, 'topleft': {'x': 558, 'y': 238}, 'bottomright': {'x': 716, 'y': 379}}, {'label': 'tvmonitor', 'confidence': 0.2524646, 'topleft': {'x': 401, 'y': 42}, 'bottomright': {'x': 697, 'y': 399}}, {'label': 'microwave', 'confidence': 0.20507553, 'topleft': {'x': 43, 'y': 333}, 'bottomright': {'x': 540, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.36070397, 'topleft': {'x': 91, 'y': 330}, 'bottomright': {'x': 544, 'y': 404}}], 0.0), ([{'label': 'diningtable', 'confidence': 0.121414885, 'topleft': {'x': 561, 'y': 239}, 'bottomright': {'x': 714, 'y': 373}}, {'label': 'tvmonitor', 'confidence': 0.10568733, 'topleft': {'x': 28, 'y': 17}, 'bottomright': {'x': 306, 'y': 250}}, {'label': 'tvmonitor', 'confidence': 0.3991819, 'topleft': {'x': 404, 'y': 24}, 'bottomright': {'x': 692, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.432798, 'topleft': {'x': 92, 'y': 327}, 'bottomright': {'x': 541, 'y': 403}}, {'label': 'microwave', 'confidence': 0.3703576, 'topleft': {'x': 76, 'y': 318}, 'bottomright': {'x': 554, 'y': 401}}], 100.0), ([{'label': 'chair', 'confidence': 0.15903777, 'topleft': {'x': 2, 'y': 219}, 'bottomright': {'x': 104, 'y': 394}}, {'label': 'chair', 'confidence': 0.18745604, 'topleft': {'x': 13, 'y': 225}, 'bottomright': {'x': 259, 'y': 398}}, {'label': 'diningtable', 'confidence': 0.16162585, 'topleft': {'x': 560, 'y': 235}, 'bottomright': {'x': 713, 'y': 380}}, {'label': 'tvmonitor', 'confidence': 0.13487224, 'topleft': {'x': 30, 'y': 9}, 'bottomright': {'x': 316, 'y': 227}}, {'label': 'tvmonitor', 'confidence': 0.10557344, 'topleft': {'x': 528, 'y': 38}, 'bottomright': {'x': 719, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.47824207, 'topleft': {'x': 112, 'y': 328}, 'bottomright': {'x': 529, 'y': 401}}, {'label': 'microwave', 'confidence': 0.41216028, 'topleft': {'x': 32, 'y': 291}, 'bottomright': {'x': 550, 'y': 404}}], 200.0), ([{'label': 'chair', 'confidence': 0.20980461, 'topleft': {'x': 1, 'y': 224}, 'bottomright': {'x': 56, 'y': 388}}, {'label': 'chair', 'confidence': 0.10808728, 'topleft': {'x': 5, 'y': 215}, 'bottomright': {'x': 265, 'y': 403}}, {'label': 'diningtable', 'confidence': 0.12779975, 'topleft': {'x': 565, 'y': 212}, 'bottomright': {'x': 713, 'y': 354}}, {'label': 'tvmonitor', 'confidence': 0.115053035, 'topleft': {'x': 27, 'y': 16}, 'bottomright': {'x': 313, 'y': 216}}, {'label': 'tvmonitor', 'confidence': 0.116568, 'topleft': {'x': 453, 'y': 40}, 'bottomright': {'x': 714, 'y': 358}}, {'label': 'tvmonitor', 'confidence': 0.30774802, 'topleft': {'x': 61, 'y': 310}, 'bottomright': {'x': 523, 'y': 403}}, {'label': 'laptop', 'confidence': 0.12993729, 'topleft': {'x': 107, 'y': 307}, 'bottomright': {'x': 530, 'y': 403}}, {'label': 'microwave', 'confidence': 0.36867908, 'topleft': {'x': 82, 'y': 292}, 'bottomright': {'x': 549, 'y': 404}}], 300.0), ([{'label': 'bird', 'confidence': 0.19501163, 'topleft': {'x': 330, 'y': 368}, 'bottomright': {'x': 378, 'y': 404}}, {'label': 'cat', 'confidence': 0.10808395, 'topleft': {'x': 198, 'y': 376}, 'bottomright': {'x': 289, 'y': 404}}, {'label': 'chair', 'confidence': 0.110156655, 'topleft': {'x': 273, 'y': 125}, 'bottomright': {'x': 440, 'y': 273}}, {'label': 'chair', 'confidence': 0.12092763, 'topleft': {'x': 5, 'y': 180}, 'bottomright': {'x': 269, 'y': 400}}, {'label': 'tvmonitor', 'confidence': 0.16968393, 'topleft': {'x': 405, 'y': 19}, 'bottomright': {'x': 695, 'y': 301}}, {'label': 'tvmonitor', 'confidence': 0.16052675, 'topleft': {'x': 562, 'y': 195}, 'bottomright': {'x': 718, 'y': 331}}, {'label': 'tvmonitor', 'confidence': 0.7032519, 'topleft': {'x': 2, 'y': 294}, 'bottomright': {'x': 575, 'y': 399}}, {'label': 'laptop', 'confidence': 0.10222144, 'topleft': {'x': 103, 'y': 263}, 'bottomright': {'x': 604, 'y': 404}}], 400.0), ([{'label': 'cat', 'confidence': 0.35772175, 'topleft': {'x': 174, 'y': 346}, 'bottomright': {'x': 393, 'y': 402}}, {'label': 'bird', 'confidence': 0.1658162, 'topleft': {'x': 328, 'y': 349}, 'bottomright': {'x': 382, 'y': 403}}, {'label': 'chair', 'confidence': 0.12223534, 'topleft': {'x': 657, 'y': 288}, 'bottomright': {'x': 718, 'y': 403}}, {'label': 'tvmonitor', 'confidence': 0.2144852, 'topleft': {'x': 405, 'y': 28}, 'bottomright': {'x': 692, 'y': 290}}, {'label': 'tvmonitor', 'confidence': 0.64373803, 'topleft': {'x': 17, 'y': 267}, 'bottomright': {'x': 559, 'y': 404}}], 500.0), ([{'label': 'person', 'confidence': 0.10750235, 'topleft': {'x': 1, 'y': 333}, 'bottomright': {'x': 44, 'y': 404}}, {'label': 'cat', 'confidence': 0.31962994, 'topleft': {'x': 174, 'y': 336}, 'bottomright': {'x': 382, 'y': 401}}, {'label': 'chair', 'confidence': 0.13275713, 'topleft': {'x': 2, 'y': 175}, 'bottomright': {'x': 55, 'y': 359}}, {'label': 'tvmonitor', 'confidence': 0.1755416, 'topleft': {'x': 409, 'y': 19}, 'bottomright': {'x': 690, 'y': 257}}, {'label': 'tvmonitor', 'confidence': 0.6187084, 'topleft': {'x': 12, 'y': 264}, 'bottomright': {'x': 564, 'y': 404}}, {'label': 'laptop', 'confidence': 0.14482969, 'topleft': {'x': 129, 'y': 253}, 'bottomright': {'x': 664, 'y': 404}}], 600.0), ([{'label': 'cat', 'confidence': 0.47887805, 'topleft': {'x': 162, 'y': 311}, 'bottomright': {'x': 403, 'y': 403}}, {'label': 'chair', 'confidence': 0.10665593, 'topleft': {'x': 61, 'y': 175}, 'bottomright': {'x': 276, 'y': 236}}, {'label': 'chair', 'confidence': 0.3392219, 'topleft': {'x': 657, 'y': 257}, 'bottomright': {'x': 718, 'y': 401}}, {'label': 'tvmonitor', 'confidence': 0.2952641, 'topleft': {'x': 410, 'y': 29}, 'bottomright': {'x': 686, 'y': 240}}, {'label': 'tvmonitor', 'confidence': 0.6430622, 'topleft': {'x': 42, 'y': 250}, 'bottomright': {'x': 527, 'y': 404}}], 700.0000000000001), ([{'label': 'cat', 'confidence': 0.7067051, 'topleft': {'x': 170, 'y': 303}, 'bottomright': {'x': 395, 'y': 399}}, {'label': 'chair', 'confidence': 0.1010209, 'topleft': {'x': 664, 'y': 245}, 'bottomright': {'x': 717, 'y': 403}}, {'label': 'tvmonitor', 'confidence': 0.1069465, 'topleft': {'x': 34, 'y': 8}, 'bottomright': {'x': 314, 'y': 182}}, {'label': 'tvmonitor', 'confidence': 0.44680485, 'topleft': {'x': 65, 'y': 239}, 'bottomright': {'x': 499, 'y': 404}}], 800.0), ([{'label': 'person', 'confidence': 0.1470381, 'topleft': {'x': 0, 'y': 85}, 'bottomright': {'x': 273, 'y': 360}}, {'label': 'person', 'confidence': 0.20587572, 'topleft': {'x': 0, 'y': 303}, 'bottomright': {'x': 41, 'y': 400}}, {'label': 'cat', 'confidence': 0.6494799, 'topleft': {'x': 183, 'y': 285}, 'bottomright': {'x': 368, 'y': 404}}, {'label': 'chair', 'confidence': 0.13149841, 'topleft': {'x': 661, 'y': 226}, 'bottomright': {'x': 719, 'y': 393}}, {'label': 'tvmonitor', 'confidence': 0.20233664, 'topleft': {'x': 408, 'y': 18}, 'bottomright': {'x': 686, 'y': 213}}, {'label': 'tvmonitor', 'confidence': 0.6835653, 'topleft': {'x': 57, 'y': 209}, 'bottomright': {'x': 580, 'y': 404}}], 900.0), ([{'label': 'person', 'confidence': 0.14286262, 'topleft': {'x': 6, 'y': 1}, 'bottomright': {'x': 59, 'y': 56}}, {'label': 'person', 'confidence': 0.27864012, 'topleft': {'x': 0, 'y': 302}, 'bottomright': {'x': 42, 'y': 402}}, {'label': 'cat', 'confidence': 0.6392344, 'topleft': {'x': 180, 'y': 276}, 'bottomright': {'x': 374, 'y': 404}}, {'label': 'chair', 'confidence': 0.120299965, 'topleft': {'x': 14, 'y': 0}, 'bottomright': {'x': 562, 'y': 366}}, {'label': 'chair', 'confidence': 0.12723537, 'topleft': {'x': 665, 'y': 207}, 'bottomright': {'x': 719, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.30947506, 'topleft': {'x': 403, 'y': 24}, 'bottomright': {'x': 697, 'y': 203}}, {'label': 'tvmonitor', 'confidence': 0.6165459, 'topleft': {'x': 81, 'y': 202}, 'bottomright': {'x': 560, 'y': 404}}], 1000.0), ([{'label': 'chair', 'confidence': 0.141772, 'topleft': {'x': 4, 'y': 21}, 'bottomright': {'x': 197, 'y': 339}}, {'label': 'diningtable', 'confidence': 0.29719263, 'topleft': {'x': 558, 'y': 238}, 'bottomright': {'x': 716, 'y': 379}}, {'label': 'tvmonitor', 'confidence': 0.2524646, 'topleft': {'x': 401, 'y': 42}, 'bottomright': {'x': 697, 'y': 399}}, {'label': 'microwave', 'confidence': 0.20507553, 'topleft': {'x': 43, 'y': 333}, 'bottomright': {'x': 540, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.36070397, 'topleft': {'x': 91, 'y': 330}, 'bottomright': {'x': 544, 'y': 404}}], 1100.0)]

listOfResultsWithoutTuple = [[{'label': 'chair', 'confidence': 0.141772, 'topleft': {'x': 4, 'y': 21}, 'bottomright': {'x': 197, 'y': 339}}, {'label': 'diningtable', 'confidence': 0.29719263, 'topleft': {'x': 558, 'y': 238}, 'bottomright': {'x': 716, 'y': 379}}, {'label': 'tvmonitor', 'confidence': 0.2524646, 'topleft': {'x': 401, 'y': 42}, 'bottomright': {'x': 697, 'y': 399}}, {'label': 'microwave', 'confidence': 0.20507553, 'topleft': {'x': 43, 'y': 333}, 'bottomright': {'x': 540, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.36070397, 'topleft': {'x': 91, 'y': 330}, 'bottomright': {'x': 544, 'y': 404}}], [{'label': 'diningtable', 'confidence': 0.121414885, 'topleft': {'x': 561, 'y': 239}, 'bottomright': {'x': 714, 'y': 373}}, {'label': 'tvmonitor', 'confidence': 0.10568733, 'topleft': {'x': 28, 'y': 17}, 'bottomright': {'x': 306, 'y': 250}}, {'label': 'tvmonitor', 'confidence': 0.3991819, 'topleft': {'x': 404, 'y': 24}, 'bottomright': {'x': 692, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.432798, 'topleft': {'x': 92, 'y': 327}, 'bottomright': {'x': 541, 'y': 403}}, {'label': 'microwave', 'confidence': 0.3703576, 'topleft': {'x': 76, 'y': 318}, 'bottomright': {'x': 554, 'y': 401}}], [{'label': 'chair', 'confidence': 0.15903777, 'topleft': {'x': 2, 'y': 219}, 'bottomright': {'x': 104, 'y': 394}}, {'label': 'chair', 'confidence': 0.18745604, 'topleft': {'x': 13, 'y': 225}, 'bottomright': {'x': 259, 'y': 398}}, {'label': 'diningtable', 'confidence': 0.16162585, 'topleft': {'x': 560, 'y': 235}, 'bottomright': {'x': 713, 'y': 380}}, {'label': 'tvmonitor', 'confidence': 0.13487224, 'topleft': {'x': 30, 'y': 9}, 'bottomright': {'x': 316, 'y': 227}}, {'label': 'tvmonitor', 'confidence': 0.10557344, 'topleft': {'x': 528, 'y': 38}, 'bottomright': {'x': 719, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.47824207, 'topleft': {'x': 112, 'y': 328}, 'bottomright': {'x': 529, 'y': 401}}, {'label': 'microwave', 'confidence': 0.41216028, 'topleft': {'x': 32, 'y': 291}, 'bottomright': {'x': 550, 'y': 404}}], [{'label': 'chair', 'confidence': 0.20980461, 'topleft': {'x': 1, 'y': 224}, 'bottomright': {'x': 56, 'y': 388}}, {'label': 'chair', 'confidence': 0.10808728, 'topleft': {'x': 5, 'y': 215}, 'bottomright': {'x': 265, 'y': 403}}, {'label': 'diningtable', 'confidence': 0.12779975, 'topleft': {'x': 565, 'y': 212}, 'bottomright': {'x': 713, 'y': 354}}, {'label': 'tvmonitor', 'confidence': 0.115053035, 'topleft': {'x': 27, 'y': 16}, 'bottomright': {'x': 313, 'y': 216}}, {'label': 'tvmonitor', 'confidence': 0.116568, 'topleft': {'x': 453, 'y': 40}, 'bottomright': {'x': 714, 'y': 358}}, {'label': 'tvmonitor', 'confidence': 0.30774802, 'topleft': {'x': 61, 'y': 310}, 'bottomright': {'x': 523, 'y': 403}}, {'label': 'laptop', 'confidence': 0.12993729, 'topleft': {'x': 107, 'y': 307}, 'bottomright': {'x': 530, 'y': 403}}, {'label': 'microwave', 'confidence': 0.36867908, 'topleft': {'x': 82, 'y': 292}, 'bottomright': {'x': 549, 'y': 404}}], [{'label': 'bird', 'confidence': 0.19501163, 'topleft': {'x': 330, 'y': 368}, 'bottomright': {'x': 378, 'y': 404}}, {'label': 'cat', 'confidence': 0.10808395, 'topleft': {'x': 198, 'y': 376}, 'bottomright': {'x': 289, 'y': 404}}, {'label': 'chair', 'confidence': 0.110156655, 'topleft': {'x': 273, 'y': 125}, 'bottomright': {'x': 440, 'y': 273}}, {'label': 'chair', 'confidence': 0.12092763, 'topleft': {'x': 5, 'y': 180}, 'bottomright': {'x': 269, 'y': 400}}, {'label': 'tvmonitor', 'confidence': 0.16968393, 'topleft': {'x': 405, 'y': 19}, 'bottomright': {'x': 695, 'y': 301}}, {'label': 'tvmonitor', 'confidence': 0.16052675, 'topleft': {'x': 562, 'y': 195}, 'bottomright': {'x': 718, 'y': 331}}, {'label': 'tvmonitor', 'confidence': 0.7032519, 'topleft': {'x': 2, 'y': 294}, 'bottomright': {'x': 575, 'y': 399}}, {'label': 'laptop', 'confidence': 0.10222144, 'topleft': {'x': 103, 'y': 263}, 'bottomright': {'x': 604, 'y': 404}}], [{'label': 'cat', 'confidence': 0.35772175, 'topleft': {'x': 174, 'y': 346}, 'bottomright': {'x': 393, 'y': 402}}, {'label': 'bird', 'confidence': 0.1658162, 'topleft': {'x': 328, 'y': 349}, 'bottomright': {'x': 382, 'y': 403}}, {'label': 'chair', 'confidence': 0.12223534, 'topleft': {'x': 657, 'y': 288}, 'bottomright': {'x': 718, 'y': 403}}, {'label': 'tvmonitor', 'confidence': 0.2144852, 'topleft': {'x': 405, 'y': 28}, 'bottomright': {'x': 692, 'y': 290}}, {'label': 'tvmonitor', 'confidence': 0.64373803, 'topleft': {'x': 17, 'y': 267}, 'bottomright': {'x': 559, 'y': 404}}], [{'label': 'person', 'confidence': 0.10750235, 'topleft': {'x': 1, 'y': 333}, 'bottomright': {'x': 44, 'y': 404}}, {'label': 'cat', 'confidence': 0.31962994, 'topleft': {'x': 174, 'y': 336}, 'bottomright': {'x': 382, 'y': 401}}, {'label': 'chair', 'confidence': 0.13275713, 'topleft': {'x': 2, 'y': 175}, 'bottomright': {'x': 55, 'y': 359}}, {'label': 'tvmonitor', 'confidence': 0.1755416, 'topleft': {'x': 409, 'y': 19}, 'bottomright': {'x': 690, 'y': 257}}, {'label': 'tvmonitor', 'confidence': 0.6187084, 'topleft': {'x': 12, 'y': 264}, 'bottomright': {'x': 564, 'y': 404}}, {'label': 'laptop', 'confidence': 0.14482969, 'topleft': {'x': 129, 'y': 253}, 'bottomright': {'x': 664, 'y': 404}}], [{'label': 'cat', 'confidence': 0.47887805, 'topleft': {'x': 162, 'y': 311}, 'bottomright': {'x': 403, 'y': 403}}, {'label': 'chair', 'confidence': 0.10665593, 'topleft': {'x': 61, 'y': 175}, 'bottomright': {'x': 276, 'y': 236}}, {'label': 'chair', 'confidence': 0.3392219, 'topleft': {'x': 657, 'y': 257}, 'bottomright': {'x': 718, 'y': 401}}, {'label': 'tvmonitor', 'confidence': 0.2952641, 'topleft': {'x': 410, 'y': 29}, 'bottomright': {'x': 686, 'y': 240}}, {'label': 'tvmonitor', 'confidence': 0.6430622, 'topleft': {'x': 42, 'y': 250}, 'bottomright': {'x': 527, 'y': 404}}], [{'label': 'cat', 'confidence': 0.7067051, 'topleft': {'x': 170, 'y': 303}, 'bottomright': {'x': 395, 'y': 399}}, {'label': 'chair', 'confidence': 0.1010209, 'topleft': {'x': 664, 'y': 245}, 'bottomright': {'x': 717, 'y': 403}}, {'label': 'tvmonitor', 'confidence': 0.1069465, 'topleft': {'x': 34, 'y': 8}, 'bottomright': {'x': 314, 'y': 182}}, {'label': 'tvmonitor', 'confidence': 0.44680485, 'topleft': {'x': 65, 'y': 239}, 'bottomright': {'x': 499, 'y': 404}}], [{'label': 'person', 'confidence': 0.1470381, 'topleft': {'x': 0, 'y': 85}, 'bottomright': {'x': 273, 'y': 360}}, {'label': 'person', 'confidence': 0.20587572, 'topleft': {'x': 0, 'y': 303}, 'bottomright': {'x': 41, 'y': 400}}, {'label': 'cat', 'confidence': 0.6494799, 'topleft': {'x': 183, 'y': 285}, 'bottomright': {'x': 368, 'y': 404}}, {'label': 'chair', 'confidence': 0.13149841, 'topleft': {'x': 661, 'y': 226}, 'bottomright': {'x': 719, 'y': 393}}, {'label': 'tvmonitor', 'confidence': 0.20233664, 'topleft': {'x': 408, 'y': 18}, 'bottomright': {'x': 686, 'y': 213}}, {'label': 'tvmonitor', 'confidence': 0.6835653, 'topleft': {'x': 57, 'y': 209}, 'bottomright': {'x': 580, 'y': 404}}], [{'label': 'person', 'confidence': 0.14286262, 'topleft': {'x': 6, 'y': 1}, 'bottomright': {'x': 59, 'y': 56}}, {'label': 'person', 'confidence': 0.27864012, 'topleft': {'x': 0, 'y': 302}, 'bottomright': {'x': 42, 'y': 402}}, {'label': 'cat', 'confidence': 0.6392344, 'topleft': {'x': 180, 'y': 276}, 'bottomright': {'x': 374, 'y': 404}}, {'label': 'chair', 'confidence': 0.120299965, 'topleft': {'x': 14, 'y': 0}, 'bottomright': {'x': 562, 'y': 366}}, {'label': 'chair', 'confidence': 0.12723537, 'topleft': {'x': 665, 'y': 207}, 'bottomright': {'x': 719, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.30947506, 'topleft': {'x': 403, 'y': 24}, 'bottomright': {'x': 697, 'y': 203}}, {'label': 'tvmonitor', 'confidence': 0.6165459, 'topleft': {'x': 81, 'y': 202}, 'bottomright': {'x': 560, 'y': 404}}], [{'label': 'chair', 'confidence': 0.141772, 'topleft': {'x': 4, 'y': 21}, 'bottomright': {'x': 197, 'y': 339}}, {'label': 'diningtable', 'confidence': 0.29719263, 'topleft': {'x': 558, 'y': 238}, 'bottomright': {'x': 716, 'y': 379}}, {'label': 'tvmonitor', 'confidence': 0.2524646, 'topleft': {'x': 401, 'y': 42}, 'bottomright': {'x': 697, 'y': 399}}, {'label': 'microwave', 'confidence': 0.20507553, 'topleft': {'x': 43, 'y': 333}, 'bottomright': {'x': 540, 'y': 404}}, {'label': 'tvmonitor', 'confidence': 0.36070397, 'topleft': {'x': 91, 'y': 330}, 'bottomright': {'x': 544, 'y': 404}}]]

myUniqueClassSet = {'laptop', 'microwave', 'chair', 'bird', 'cat', 'person', 'diningtable', 'tvmonitor'}

myClassDict = {0: 'chair', 1: 'diningtable', 2: 'tvmonitor', 3: 'microwave', 4: 'laptop', 5: 'bird', 6: 'cat', 7: 'person'}

confidenceDict = {0: 2.35993893, 1: 1.005225745, 2: 9.411997535, 3: 1.5613480199999998, 4: 0.37698842, 5: 0.36082782999999996, 6: 3.2597330899999997, 7: 0.88191891}

numberOfTimesEmergedDict = {0: 16, 1: 5, 2: 28, 3: 5, 4: 3, 5: 2, 6: 7, 7: 5}

averageConfidenceDict = {0: 0.147496183125, 1: 0.20104514899999998, 2: 0.33614276910714286, 3: 0.312269604, 4: 0.12566280666666665, 5: 0.18041391499999998, 6: 0.46567615571428567, 7: 0.176383782}

def sortDictInDescendingOrder(_myDict):
    return {k: v for k, v in reversed(sorted(_myDict.items(), key=lambda item: item[1]))}

def getDetectedforDatabase(_myDict,_averageConfidenceDict):
    # print("Before Sorting....")
    # print("Class Dictionary : ")
    # print(_myDict)
    # print("Average Confidence Dictionary : ")
    # print(_averageConfidenceDict)

    # print("\nAfter Sorting In Descending Order....")
    newSortedDictWithRequiredKey = sortDictInDescendingOrder(_averageConfidenceDict)
    # print("newSortedDictWithRequiredKey : ")
    # print(newSortedDictWithRequiredKey)

    counter=0
    newSortedAvgConfidenceDictWithRequiredNumber=dict()
    newSortedClassDict=dict()

    for a in newSortedDictWithRequiredKey.keys():
        #print("counter = {:d} and counter = {:d}".format(counter,_number))
        # if counter == _number:
        #     break
        newSortedAvgConfidenceDictWithRequiredNumber[counter]=newSortedDictWithRequiredKey[a]
        newSortedClassDict[counter] = _myDict[a]
        counter = counter + 1

    outputstring=""
    for a in range(len(newSortedClassDict)):
    	score = (len(newSortedClassDict)-a)/len(newSortedClassDict)
    	outputstring+=newSortedClassDict[a]+":"+str(score)
    	if a<(len(newSortedClassDict)-1):
    		outputstring+="|"

    return outputstring

    # return newSortedClassDict,newSortedAvgConfidenceDictWithRequiredNumber

# getDetectedforDatabase(myClassDict,averageConfidenceDict)




# newSortedDictWithRequiredNumber = {0: 0.46567615571428567, 1: 0.33614276910714286, 2: 0.312269604}
# newSortedClassDict = {0: 'cat', 1: 'tvmonitor', 2: 'microwave'}
# See here if the dict is only length 3: 
# {0: 'cat', 1: 'tvmonitor', 2: 'microwave'}



# detectedobjectinformation = makeinfodatabasewritable(myClassDict,averageConfidenceDict)



# #x=int(input("Enter the number of classes with highest confidence : "))
# x=3
# newSortedClassDict,newSortedAvgConfidenceDictWithRequiredNumber = arrangeNnumberOfDictionary(x,myClassDict,averageConfidenceDict)


# # detectedobjectinformation = makeinfodatabasewritable(myClassDict,averageConfidenceDict)


# print("See here if the dict is only length 3: ")
# print(newSortedClassDict)
# finalJsonArray = returnList(newSortedClassDict,listOfResultsWithTuple)

# # _analyticsFileUploadTime=datetime.utcnow()
# # analyticsstartingdt_string = _analyticsFileUploadTime.strftime("%Y%m%d%H%M%S")
# # analyticsFileName = analyticsstartingdt_string+_videofilename.split('.')[0]+".json"
# # writeListAsAJsonFile(finalJsonArray,analyticsFileName)

# # generatedAnalyticsFile = VideoAnalyticsFile(filename=analyticsFileName,storagelocation=app.config["VIDEOANALYTICS_GENERATED_FOLDER"],createdTime = _analyticsFileUploadTime,videoFile=_uploadedVideo)
# # db.session.add(generatedAnalyticsFile)
# # db.session.commit()

# # generatedVideoStartingTime=datetime.utcnow()
# # gen_video_dt_string = generatedVideoStartingTime.strftime("%Y%m%d%H%M%S")
# # generatedVideoFilename = gen_video_dt_string+"_generated_"+_videofilename.split('.')[0]

# # indexOfRequiredFrame=extractIndicesFromTuple(listOfResultsWithTuple,newSortedClassDict)


# # frameToVid(indexOfRequiredFrame,originalFrameArray,newframeArray,app.config['VIDEO_GENERATED_FOLDER']+"/"+generatedVideoFilename+".webm", fps)
# #frameToVid(listOfResultsWithTuple,newSortedClassDict,originalFrameArray,newframeArray,app.config['VIDEO_GENERATED_FOLDER']+"/"+generatedVideoFilename,fps)

# # generatedVideo = GeneratedVideo(filename = generatedVideoFilename,storagelocation = app.config['VIDEO_GENERATED_FOLDER'],createdTime = generatedVideoStartingTime,video_id = _uploadedVideo.videoid)
# # db.session.add(generatedVideo)
# # db.session.commit()
