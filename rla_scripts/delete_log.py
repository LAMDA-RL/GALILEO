"""
A script to delete useless experimental logs by regex string.

"""
from RLA.easy_log.log_tools import DeleteLogTool, Filter
import argparse

def argsparser():
    parser = argparse.ArgumentParser("Delete Log")
    # reduce setting
    parser.add_argument('--sub_proj', type=str, default="")
    parser.add_argument('--task', type=str, default="")
    parser.add_argument('--reg', type=str)
    parser.add_argument('--timestep_bound', type=int, default=100)
    parser.add_argument('--delete_type', type=str, default=Filter.ALL)


    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = argsparser()
    filter = Filter()
    filter.config(type=args.delete_type, timstep_bound=args.timestep_bound)
    dlt = DeleteLogTool(proj_root='./', sub_proj=args.sub_proj, task=args.task, regex=args.reg,
                        filter=filter)
    if args.delete_type == Filter.ALL:
        dlt.delete_related_log()
    elif args.delete_type == Filter.SMALL_TIMESTEP:
        dlt.delete_small_timestep_log()
    else:
        raise NotImplementedError