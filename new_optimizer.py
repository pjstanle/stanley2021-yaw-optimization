import numpy as np

class GF1():

    def __init__(self):

        # inputs
        self.objective_function = None # takes design_variables as an input and outputs the objective values (needs to account for any constraints already)
        self.bounds = np.array([]) # array of tuples same length as design_variables
        self.n_leaders = 0
        self.n_followers = 0
        self.new_leaders = 0
        self.replace_leaders = 0
        self.start_radius = 0.25
        self.alpha = 1.0       
        self.convergence_iters = 10 

        # internal variables
        self.n_vars = 0 # number of design variable
        self.leaders = np.array([])
        self.leader_score = np.array([])
        self.temp_leaders = np.array([])
        self.search_radius = np.array([])

        # outputs
        self.solution = 0.0
        self.optimal_dvs = np.array([])


    def search_for_leaders(self,N):

        self.temp_leaders = np.zeros((N,self.n_vars))
        self.temp_leader_score = np.zeros(N)
        for i in range(N):
            for j in range(self.n_vars):
                self.temp_leaders[i,j] = np.random.rand()*(self.bounds[j,1]-self.bounds[j,0]) + self.bounds[j,0]
            self.temp_leader_score[i] = self.objective_function(self.temp_leaders[i])

    
    def search_for_followers(self):
        follower = np.zeros(self.n_vars)
        for i in range(self.n_leaders):
            for j in range(self.n_followers):
                # find the follower
                for k in range(self.n_vars):
                    # should this be a different distribution?
                    follower[k] = self.leaders[i,k] + (np.random.rand()-0.5)*(self.bounds[k,1]-self.bounds[k,0])*self.search_radius[i]
                    if follower[k] > self.bounds[k,1]:
                        follower[k] = self.bounds[k,1]
                    elif follower[k] < self.bounds[k,0]:
                        follower[k] = self.bounds[k,0]
                # evaluate the follower
                follower_score = self.objective_function(follower)
                if follower_score < self.leader_score[i]:
                    self.leaders[i] = follower
                    self.leader_score[i] = follower_score

    
    def optimize(self):

        # initialize
        self.n_vars = np.shape(self.bounds)[0]
        self.leaders = np.zeros((self.n_leaders,self.n_vars))
        self.leader_score = np.zeros(self.n_leaders)
        self.search_radius = np.ones(self.n_leaders)*self.start_radius

        self.search_for_leaders(self.n_leaders)
        self.leaders[:] = self.temp_leaders[:]
        self.leader_score[:] = self.temp_leader_score[:]

        converged = False

        # print("start: ", self.leader_score)
        before_list = np.zeros(self.n_leaders)
        # for k in range(100000):
        iter_counter = 0
        old_best = np.min(self.leader_score)
        while not converged:
            # local search around each top point
            before_list[:] = self.leader_score[:]
            self.search_for_followers()
            for i in range(self.n_leaders):
                if self.leader_score[i] < before_list[i]:
                    self.search_radius[i] *= self.alpha
                # else:
                #     self.search_radius[i] /= self.alpha

            # fully random search for new leaders
            self.search_for_leaders(self.new_leaders)
            
            # if min(self.temp_leader_score) < max(self.leader_score):
            #     print("before: ", self.leaders)
            #     print(self.leader_score)
            #     # just take the best leaders
            #     list_of_performance = np.append(self.leader_score,self.temp_leader_score)
            #     list_of_leaders = np.zeros((self.n_leaders+self.new_leaders,self.n_vars))
                
            #     new_radius = np.zeros(self.new_leaders) + self.start_radius
            #     list_of_radii = np.append(self.search_radius,new_radius)
            #     for i in range(self.n_leaders):
            #         list_of_leaders[i][:] = self.leaders[i][:]
            #     for i in range(self.new_leaders):
            #         list_of_leaders[i+self.n_leaders][:] = self.temp_leaders[i][:]
            #     order = np.argsort(list_of_performance)
                
            #     for i in range(self.n_leaders):
            #         self.leaders[i][:] = list_of_leaders[order[i]][:]
            #         self.leader_score[i] = list_of_performance[order[i]]
                
            # else:

            sorted_order = np.argsort(self.leader_score)

            new_order = np.argsort(self.temp_leader_score)
            new_sorted_leaders = np.zeros_like(self.temp_leaders)
            for i in range(self.new_leaders):
                new_sorted_leaders[i][:] = self.temp_leaders[new_order[i]][:]
            new_sorted_scores = np.sort(self.temp_leader_score)

            # print("before: ", self.leader_score)
            # print(self.leaders)
            for i in range(self.replace_leaders):
                self.leaders[sorted_order[-(i+1)],:] = new_sorted_leaders[i,:]
                self.leader_score[sorted_order[-(i+1)]] = new_sorted_scores[i]
                self.search_radius[sorted_order[-(i+1)]] = self.start_radius
            # print("after: ", self.leader_score)
            # print(self.leaders)

            # current_order = np.argsort(self.leader_score)
            # sorted_leaders = np.zeros_like(self.leaders)
            # for i in range(self.n_leaders):
            #     sorted_leaders[i][:] = self.leaders[current_order[i]][:]
            # self.leaders[:] = sorted_leaders[:]
            # self.leader_score = np.sort(self.leader_score)

            # new_order = np.argsort(self.temp_leader_score)
            # new_sorted_leaders = np.zeros_like(self.temp_leaders)
            # for i in range(self.new_leaders):
            #     new_sorted_leaders[i][:] = self.temp_leaders[new_order[i]][:]
            # new_sorted_scores = np.sort(self.temp_leader_score)

            # for i in range(self.replace_leaders):
            #     self.leaders[-(i+1),:] = new_sorted_leaders[i,:]
            #     self.leader_score[-(i+1)] = new_sorted_scores[i]

                

            # print("current: ", self.leaders)
            # print(self.leader_score)

            # print("random: ", self.temp_leaders)
            # print(self.temp_leader_score)

            if np.min(self.leader_score) == old_best:
                iter_counter += 1
            
            else:
                old_best = np.min(self.leader_score)
            
            if iter_counter == self.convergence_iters:
                converged = True

            print(old_best)

        # print("end: ", self.leader_score)
        # print(min(self.leader_score))

        self.solution = min(self.leader_score)
        self.optimal_dvs = self.leaders[np.argmin(self.leader_score)]






    


if __name__=="__main__":


    def dummy1(x):
        return np.sum(x)

    def simple_obj(x):
        return x[0]+x[1]

    def rosenbrock_obj(x):
        return (1-x[0])**2 + 100.0*(x[1]-x[0]**2)**2

    def ackley_obj(x):
        global func_calls
        func_calls += 1
        p1 = -20.0*np.exp(-0.2*np.sqrt(0.5*(x[0]**2+x[1]**2)))
        p2 = np.exp(0.5*(np.cos(2.*np.pi*x[0]) + np.cos(2.0*np.pi*x[1]))) + np.e + 20.0
        return p1-p2

    def rastrigin_obj(x):
        global func_calls
        func_calls += 1
        A = 10.0
        n = len(x)
        tot = 0
        for i in range(n):
            tot += x[i]**2 - A*np.cos(2.0*np.pi*x[i])
        return A*n + tot


    # import matplotlib.pyplot as plt

    # from mpl_toolkits.mplot3d import Axes3D
    # X = np.arange(-5, 5, 0.02)
    # Y = np.arange(-5, 5, 0.02)
    # X, Y = np.meshgrid(X, Y)
    # Z = np.zeros_like(X)
    # for i in range(np.shape(Z)[0]):
    #     for j in range(np.shape(Z)[1]):
    #         Z[i][j] = rastrigin_obj(np.array([X[i][j],Y[i][j]]))
    #         # Z[i][j] = ackley_obj(np.array([X[i][j],Y[i][j]]))
    
    # # Plot the surface.
    # fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # surf = ax.plot_surface(X, Y, Z,linewidth=0, antialiased=False)

    
    global func_calls
    func_calls = 0

    N = 20
    n_runs = 30
    solutions = np.zeros((N,n_runs))
    alphas = np.linspace(0.1,1.0,N)
    for k in range(N):
        print(k)
        for j in range(n_runs):

            optimizer = GF1()
            bounds = np.array([(-5.0,5.),(-5.,5.)])
            optimizer.bounds = bounds
            optimizer.objective_function = ackley_obj
            optimizer.n_leaders = 5
            optimizer.new_leaders = 5
            optimizer.replace_leaders = 1
            optimizer.n_followers = 20
            optimizer.start_radius = 0.5
            optimizer.alpha = alphas[k]
            optimizer.convergence_iters = 20

            optimizer.optimize()
            solutions[k,j] = optimizer.solution
    
    import matplotlib.pyplot as plt

    for k in range(N):
        plt.scatter(np.zeros(n_runs)+alphas[k],solutions[k,:])
    plt.show()
        # print(rastrigin_obj([0.,0.]))
        # print("function calls: ", func_calls)

    # plt.show()