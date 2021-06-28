import java.util.map

def checkoutScm(Map config) {
    String pScmUrl = "url"
    String pScmBranch = "branch"
  
    String scmUrl = config.get(pScmUrl.trim())
    String scmBranch = config.get(pScmBranch)
    dir(dstDir) {
        git url: scmUrl,
            branch: scmBranch,
  }
}

return this
