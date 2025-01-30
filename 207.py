class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph=defaultdict(list)
        indegree=[0]*numCourses

        for preq, course in prerequisites:
            graph[preq].append(course)
            indegree[course]+=1

        #initalize a queue
        queue=deque([i for i in range(numCourses) if indegree[i]==1])

        course_resolved=0
        while queue:
            course=queue.popleft()
            course_resolved+=1

            for next_couse in graph[course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    queue.append(next_course)
        
        return course_resolved==numCourses