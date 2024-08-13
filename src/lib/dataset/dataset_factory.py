from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pycocotools.coco as coco
from pycocotools.cocoeval import COCOeval
import numpy as np
import json
import os

from .datasets.coco import COCO
from .datasets.coco_hp import COCOHP
from .datasets.crowdhuman import CrowdHuman
from .datasets.mot17 import MOT17
from .datasets.dancetrack import DanceTrack

dataset_factory = {
  'coco': COCO,
  'coco_hp': COCOHP,
  'crowdhuman': CrowdHuman,
  'mot17': MOT17,
  'dancetrack': DanceTrack
}

def get_dataset(dataset):
  return dataset_factory[dataset]
