class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<prerequisites.length;i++) {
            map.put(prerequisites[i][0], prerequisites[i][1]);
        }
        boolean[] visited = new boolean[numCourses];
        for(int i=0;i<prerequisites.length;i++) {
            int curr = prerequisites[i][0];
           if(visited[curr]) continue;
           int j=map.getOrDefault(curr, -1);
            while(j!=-1 &&!visited[j]) {
                visited[j]=true;
                j = map.getOrDefault(j, -1);
                count++;
            }
        }
        return true;
    }
}

//https://neetcode.io/problems/course-schedule/
