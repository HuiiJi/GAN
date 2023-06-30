import torch
import torch.nn as nn
from GAN_ import Config, Gnet
import torchvision


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') #定义模型在GPU的cuda下跑,没有cuda则在CPU慢慢跑

opt = Config() #实例化Config
g_net = Gnet(opt) #实例化生成模型
g_net = g_net.to(device)


ckpt = 'snapshots/gnet.pth' #生成网络训练好后weights的地址,也可以ckpt=opt.g_net_path
ckpt_dict = torch.load(ckpt) #将weights的字典加载出来
g_net.load_state_dict(ckpt_dict) #将字典化的weights加载进生成模型，即该模型填充了训练好的weights
g_net.eval()

input_noise = torch.randn(opt.batch_size, opt.noise_dim, 1, 1).to(device) #输入定义为正态分布的噪声
out_img = g_net(input_noise) #噪声进入生成模型，推理得到image

torchvision.utils.save_image(out_img.data[0], "%s/inference.png" % (opt.result_save_path), normalize=True) #保存image
