import torch
import torch.nn as nn
from .common import *

def MLP(in_features=2, out_features=3, hidden_features=128):


    model = nn.Sequential(
        nn.Linear(
            in_features,
            hidden_features,
              ),
        nn.ReLU(),

        nn.Linear(
            hidden_features,
            hidden_features,
              ),
        nn.ReLU(),
        
        nn.Linear(
            hidden_features,
            hidden_features,
              ),
        nn.ReLU(),

        nn.Linear(
            hidden_features,
            hidden_features,
              ),
        nn.ReLU(),
        
        nn.Linear(
            hidden_features,
            out_features,
              ),
        
    )
    
#
    return model

def conv_layers_no_GRFF(num_input_channels=2, num_output_channels=2, need_sigmoid = True, need_tanh = False):


    model = nn.Sequential(
        nn.Conv2d(
            num_input_channels,
            64,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
        nn.BatchNorm2d(64),

        nn.Conv2d(
            64,
            128,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
#         nn.BatchNorm2d(256),

        nn.Conv2d(
            128,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
#         nn.BatchNorm2d(256),
        
        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
#         nn.BatchNorm2d(256),
        
        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
#         nn.BatchNorm2d(256),
        
        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
#         nn.BatchNorm2d(256),
        
        nn.Conv2d(
            256,
            num_output_channels,
            kernel_size=1,
            padding=0),
#         nn.Sigmoid(),
    )
    if need_sigmoid:
        model.add(nn.Sigmoid())
    elif need_tanh:
        model.add(nn.Tanh())
#
    return model

def conv_layers(num_input_channels=256, num_output_channels=2, num_hidden=1000,need_sigmoid = True, need_tanh = False):


    model = nn.Sequential(
        nn.Conv2d(
            num_input_channels,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
        nn.BatchNorm2d(256),

        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
#         nn.BatchNorm2d(256),

        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
#         nn.BatchNorm2d(256),

        nn.Conv2d(
            256,
            num_output_channels,
            kernel_size=1,
            padding=0),
#         nn.Sigmoid(),
    )
    if need_sigmoid:
        model.add(nn.Sigmoid())
    elif need_tanh:
        model.add(nn.Tanh())
#
    return model

def conv_3layers(num_input_channels=256, num_output_channels=2, num_hidden=1000,need_sigmoid = True, need_tanh = False):


    model = nn.Sequential(
        nn.Conv2d(
            num_input_channels,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
        nn.BatchNorm2d(256),

        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),

#         nn.Conv2d(
#             256,
#             256,
#             kernel_size=1,
#             padding=0),
#         nn.ReLU(),

        nn.Conv2d(
            256,
            num_output_channels,
            kernel_size=1,
            padding=0),
#         nn.Sigmoid(),
    )
    if need_sigmoid:
        model.add(nn.Sigmoid())
    elif need_tanh:
        model.add(nn.Tanh())
#
    return model

def conv_2layers(num_input_channels=256, num_output_channels=2, num_hidden=1000,need_sigmoid = True, need_tanh = False):


    model = nn.Sequential(
        nn.Conv2d(
            num_input_channels,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
        nn.BatchNorm2d(256),

#         nn.Conv2d(
#             256,
#             256,
#             kernel_size=1,
#             padding=0),
#         nn.ReLU(),

#         nn.Conv2d(
#             256,
#             256,
#             kernel_size=1,
#             padding=0),
#         nn.ReLU(),

        nn.Conv2d(
            256,
            num_output_channels,
            kernel_size=1,
            padding=0),
#         nn.Sigmoid(),
    )
    if need_sigmoid:
        model.add(nn.Sigmoid())
    elif need_tanh:
        model.add(nn.Tanh())
#
    return model

def conv_6layers(num_input_channels=256, num_output_channels=2, num_hidden=1000,need_sigmoid = True, need_tanh = False):


    model = nn.Sequential(
        nn.Conv2d(
            num_input_channels,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
        nn.BatchNorm2d(256),

        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),

        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),
        
        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),

        nn.Conv2d(
            256,
            256,
            kernel_size=1,
            padding=0),
        nn.ReLU(),        

        nn.Conv2d(
            256,
            num_output_channels,
            kernel_size=1,
            padding=0),
#         nn.Sigmoid(),
    )
    if need_sigmoid:
        model.add(nn.Sigmoid())
    elif need_tanh:
        model.add(nn.Tanh())
#
    return model











