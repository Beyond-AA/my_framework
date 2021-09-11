import torch


class argparse():
    def epoch(self, epoch):
        return int(epoch)
    def lealearning_rate(self, learning_rate):
        return float(learning_rate)
    def patience(self, patience):
        return int(patience)
    def hidden_size(self, hidden_size):
        return int(hidden_size)
    def input_size(self, input_size):
        return int(input_size)
    def device(self, device):
        return device


args = argparse()
args.epoch, args.learning_rate, args.patience = [1000, 0.001, 4]
args.hidden_size, args.input_size = [40, 30]
args.device, = [torch.device("cuda:0" if torch.cuda.is_available() else "cpu"), ]
